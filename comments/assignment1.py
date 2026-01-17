public class OrderProcessor
{
    private readonly IPaymentGateway _paymentGateway;
    private readonly IInventoryService _inventoryService;
    private readonly INotificationService _notificationService;

    public OrderProcessor(
        IPaymentGateway paymentGateway,
        IInventoryService inventoryService,
        INotificationService notificationService)
    {
        _paymentGateway = paymentGateway;
        _inventoryService = inventoryService;
        _notificationService = notificationService;
    }

    public async Task<OrderResult> ProcessOrder(Order order)
    {
        if (order == null)
        {
            throw new ArgumentNullException(nameof(order));
        }

        if (!IsValidOrder(order))
        {
            return OrderResult.Invalid("Order validation failed");
        }

        if (!await _inventoryService.CheckAvailability(order.Items))
        {
            return OrderResult.Failed("Insufficient inventory");
        }

        await _inventoryService.ReserveItems(order.Items);

        try
        {
            var paymentResult = await _paymentGateway.ProcessPayment(
                order.CustomerId,
                order.TotalAmount,
                order.PaymentMethod);

            if (!paymentResult.IsSuccessful)
            {
                await _inventoryService.ReleaseReservation(order.Items);
                return OrderResult.Failed($"Payment failed: {paymentResult.ErrorMessage}");
            }

            await _inventoryService.CommitReservation(order.Items);
            await _notificationService.SendOrderConfirmation(order);

            return OrderResult.Success(paymentResult.TransactionId);
        }
        catch
        {
            // TODO: Add structured logging with correlation ID for production diagnostics
            await _inventoryService.ReleaseReservation(order.Items);
            throw;
        }
    }

    private bool IsValidOrder(Order order)
    {
        // TODO: Extend validation to check customer status and item-level pricing consistency
        return order.Items?.Count > 0 && order.TotalAmount > 0;
    }

    public async Task CancelOrder(string orderId)
    {
        var order = await GetOrderById(orderId);

        if (order.Status == OrderStatus.Paid)
        {
            await _paymentGateway.RefundPayment(order.TransactionId);
            await _inventoryService.RestoreInventory(order.Items);
        }

        order.Status = OrderStatus.Cancelled;

        // TODO: Emit domain event for order cancellation notifications
        await SaveOrder(order);
    }

    private async Task<Order> GetOrderById(string orderId)
    {
        // TODO: Replace stub with repository/database implementation
        return await Task.FromResult(new Order());
    }

    private async Task SaveOrder(Order order)
    {
        // TODO: Implement persistence logic using repository pattern
        await Task.CompletedTask;
    }
}


Through this exercise, I learned that most comments are unnecessary when code is well named and structured. Bad comments such as redundant, noise, misleading, and journal comments increase maintenance cost and reduce readability. Clean Code encourages removing such comments and writing self-explanatory code. Good comments should explain intent, business rules, or reasons that cannot be expressed clearly through code alone.