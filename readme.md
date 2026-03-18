
# Coding Guidelines

## 1. Naming

* Names must be clear, meaningful, and easy to pronounce and search.
* Avoid abbreviations, prefixes, encodings, and unnecessary filler words.
* Use single-letter variables only for short loops (`i`, `j`, `k`).

### Naming Conventions

* **Classes & Files:** UpperCamelCase
* **Methods, Variables, Fields, Parameters:** lowerCamelCase
* **Constants:** UPPER_SNAKE_CASE
* **Packages:** lowercase

### Best Practices

* Avoid names that differ only slightly.
* Use one consistent term per concept (e.g., always use `get`, not mix with `fetch` or `retrieve`).

---

## 2. Functions

* Keep functions small (preferably under 20 lines).
* Each function should perform only one task.
* Maintain a single level of abstraction per function.

### Guidelines

* Use descriptive, meaningful names.
* Minimize parameters:

  * Prefer no parameters.
  * If more than 2–3 are needed, use an object.
* Avoid boolean parameters; split into separate methods.
* Avoid side effects.
* Follow the **DRY (Don't Repeat Yourself)** principle.

---

## 3. Comments

* Prefer self-explanatory code over comments.

### Acceptable Uses

* Legal/license information
* Clarifying intent or complex logic
* Warnings and important notes
* TODOs
* Public API documentation

### Avoid

* Redundant or obvious comments

* Change logs or history comments

* Commented-out code

* Closing-brace comments

* Always place comments **above** the code they describe.

---

## 4. Formatting

### Vertical Formatting

* Use blank lines to separate logical sections.
* Keep related code together.
* Separate unrelated code clearly.
* Follow the **Stepdown Rule** (caller methods above called methods).
* Keep files under 500 lines.
* End each file with exactly one newline.

### Horizontal Formatting

* Limit lines to 120 characters.
* Use one tab per indentation level.
* Add spaces around operators: `a = b + c`
* No space before method parentheses: `runTask()`
* Always use braces `{}` for all control statements.

---

## 5. Classes

* One top-level class per file.
* File name must match the class name.

### Principles

* Each class should have a single responsibility.
* Keep fields private.
* Expose behavior via methods, not raw data.
* Ensure high cohesion.

### Member Order

1. Constants
2. Static fields
3. Instance fields
4. Constructors
5. Public methods
6. Private methods

---

## 6. Error Handling

* Use exceptions instead of return codes.
* Provide meaningful error messages.
* Do not return `null`:

  * Use empty collections or `Optional`.
* Avoid passing `null` unless required.
* Prefer unchecked exceptions.

---

## 7. Objects vs Data Structures

* **Objects:** Hide data, expose behavior.

* **Data Structures:** Expose data, no behavior.

* Avoid mixing both roles.

### Law of Demeter

* A method should only interact with its immediate dependencies.

---

## 8. SOLID Principles

* **Single Responsibility:** One reason to change per class
* **Open/Closed:** Extend without modifying existing code
* **Liskov Substitution:** Subtypes must replace base types safely
* **Interface Segregation:** Prefer small, focused interfaces
* **Dependency Inversion:** Depend on abstractions, not implementations

---

## 9. Code Smells to Eliminate

* Remove dead code (don’t comment it out).
* Replace magic numbers with named constants.
* Fix feature envy (move logic to the right class).
* Avoid primitive obsession (use domain objects).
* Reduce long parameter lists (use objects).
* Prevent scattered changes (maintain proper responsibilities).
* Avoid tight coupling between classes.


