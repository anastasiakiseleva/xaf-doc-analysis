---
uid: DevExpress.ExpressApp.Xpo.CalculatedPersistentAliasAttribute.CalculatedAliasPropertyName
name: CalculatedAliasPropertyName
type: Property
summary: Specifies the name of a property which returns the persistent alias' expression.
syntax:
  content: public string CalculatedAliasPropertyName { get; }
  parameters: []
  return:
    type: System.String
    description: A string holding the name of the public static property which returns the alias' expression.
seealso: []
---
Note that a property which returns the persistent alias' expression must be declared as `public` and `static`.