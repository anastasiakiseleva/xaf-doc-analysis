---
uid: DevExpress.Persistent.Validation.IRule.UsedProperties
name: UsedProperties
type: Property
summary: Specifies the names of the properties to be highlighted when the current [Validation Rule](xref:113008) is broken.
syntax:
  content: ReadOnlyCollection<string> UsedProperties { get; }
  parameters: []
  return:
    type: System.Collections.ObjectModel.ReadOnlyCollection{System.String}
    description: A **ReadOnlyCollection\<String>** object representing a list of the property names that must be highlighted as invalid when the Validation Rule is broken.
seealso: []
---
The [Validation Module](xref:113684) can highlight [Property Editors](xref:112612) in a [View](xref:112611) when a Validation Rule is broken. When implementing the [](xref:DevExpress.Persistent.Validation.IRule) interface, to highlight properties containing invalid values, pass the required property names via the **UsedProperties** property. 

# [C#](#tab/tabid-csharp)

```csharp
using System.Collections.ObjectModel;
// ...
public override ReadOnlyCollection<string> UsedProperties {
    get {
        return new ReadOnlyCollection<string>(new List<string>() { "Amount" });
    }
}
```
***

> [!IMPORTANT]
> Always define **UsedProperties** for _warning_ and _info_ rules.