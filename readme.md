1. Naming

Names should clearly express their purpose, be easy to say, and easy to search.

Avoid:

Shortened forms, prefixes, or unnecessary filler words

Cryptic or encoded naming styles

Use single-letter names only for simple loop counters like i, j, or k.

Follow consistent naming styles:

Classes and files → UpperCamelCase

Methods, variables, fields, parameters → lowerCamelCase

Constants → UPPER_SNAKE_CASE

Packages → lowercase

Do not use names that are too similar to each other.
Choose one term per concept and stick to it consistently (e.g., use only “get” instead of mixing “fetch” or “retrieve”).

2. Functions

Functions should be small (preferably under 20 lines) and focused on a single task.

Guidelines:

Each function should operate at one level of abstraction

Prefer clear, descriptive names over short ones

Keep parameters minimal (ideally none; if many are needed, wrap them in an object)

Avoid boolean parameters — create separate functions instead

Prevent hidden side effects; functions should behave exactly as their names suggest

Eliminate duplication by following the DRY principle

3. Comments

Rely on clean, readable code instead of comments whenever possible.

Use comments only when necessary, such as:

Legal or license information

Explaining intent or non-obvious decisions

Warnings or important notes

TODOs

Documentation for public APIs

Avoid:

Obvious or repetitive comments

Change history logs

Commented-out code

Labels for closing braces or positions

Place comments above the code they describe.

4. Formatting
Vertical Formatting

Use blank lines to separate logical sections

Keep related code close together

Separate unrelated code clearly

Follow the Stepdown Rule: higher-level methods should appear before the ones they call

Keep files under 500 lines

End each file with exactly one newline

Horizontal Formatting

Limit lines to 120 characters

Use one tab per indentation level

Add spaces around operators (a = b + c)

Do not add spaces before method parentheses (runTask(), not runTask ())

Always include braces {} even for single-line blocks

5. Classes

Each file should contain only one top-level class, and the file name must match the class name.

Class design principles:

A class should have a single responsibility

Keep fields private and expose behavior through methods

Aim for high cohesion (methods should use the class’s data)

Member order:

Constants

Static fields

Instance fields

Constructors

Public methods

Private methods

6. Error Handling

Use exceptions instead of return codes

Include helpful, meaningful error messages

Avoid returning null; use empty collections or Optional instead

Do not pass null unless absolutely required by an API

Prefer unchecked exceptions to keep APIs clean

7. Objects vs Data Structures

Objects should encapsulate data and expose behavior

Data structures should expose data without behavior

Avoid mixing these roles

Follow the Law of Demeter:

A method should only interact with its direct collaborators, not deeply nested objects

8. SOLID Principles

Single Responsibility: A class should have only one reason to change

Open/Closed: Extend behavior without modifying existing code

Liskov Substitution: Subtypes must work seamlessly in place of base types

Interface Segregation: Prefer multiple focused interfaces over one large one

Dependency Inversion: Depend on abstractions, not concrete implementations

9. Code Smells to Avoid

Remove unused (dead) code completely

Replace hardcoded values with named constants

Move logic to the class where it belongs (avoid feature envy)

Replace primitive types with meaningful domain objects when possible

Avoid long parameter lists — use objects instead

Prevent scattered changes across multiple classes by keeping responsibilities well-defined

Avoid tight coupling where classes access each other’s internal details
