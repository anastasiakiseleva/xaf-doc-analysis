---
uid: DevExpress.ExpressApp.Security.SecurityStrategy.AnonymousAllowedTypes
name: AnonymousAllowedTypes
type: Property
summary: Specifies types that users can access anonymously before they log in.
syntax:
  content: |-
    [Browsable(false)]
    public IList<Type> AnonymousAllowedTypes { get; }
  parameters: []
  return:
    type: System.Collections.Generic.IList{System.Type}
    description: A list of types that users can access anonymously.
seealso: []
---
Anonymous access may be required when you use custom logon parameters and want to display certain data in the logon window before a user logs on. Add the required types to the **AnonymousAllowedTypes** collection to grant access to these types before a successful user authentication. This code should be executed before the application displays the logon window.

The following examples demonstrate how to specify this property:

[!include[](~/templates/register-AnonymousAllowedTypes.md)]