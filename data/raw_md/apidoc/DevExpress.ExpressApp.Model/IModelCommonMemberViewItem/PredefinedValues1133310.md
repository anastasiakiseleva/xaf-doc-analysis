---
uid: DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.PredefinedValues
name: PredefinedValues
type: Property
summary: Specifies predefined values for the current Property Editor, separated by semicolons.
syntax:
  content: |-
    [ModelBrowsable(typeof(StringPropertyOnlyCalculator))]
    string PredefinedValues { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string that specifies predefined values for the current Property Editor, separated by semicolons.
seealso: []
---
Use this property with string type properties. Users can select one of predefined values or enter a custom value.

To include a semicolon in a predefined value, type `\\;`.

To include a backslash in a predefined value, type `\\`.

You can specify the `PredefinedValues` value in the [Model Editor](xref:112582).

![IModelCommonMemberViewItem.PredefinedValues](~/images/imodelcommonmemberviewitem.predefinedvalues121619.png)

Alternatively, you can use [ModelDefaultAttribute](xref:DevExpress.ExpressApp.Model.ModelDefaultAttribute) to specify predefined values in code.

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
[ModelDefault("PredefinedValues",
    "Predefined Value 1;Predefined Value 2;Predefined Value 3;Predefined Value 4")]
public virtual string StringWithPredefinedValuesProperty { get; set; }
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
[ModelDefault("PredefinedValues",
   "Predefined Value 1;Predefined Value 2;Predefined Value 3;Predefined Value 4")]
public string StringWithPredefinedValuesProperty {
    get => stringWithPredefinedValuesProperty;
    set => SetPropertyValue(nameof(StringWithPredefinedValuesProperty), ref stringWithPredefinedValuesProperty, value);
}
```
***

If you want to fill the predefined values list dynamically, use a custom property editor demonstrated in the following help topic: [How to: Implement a Property Editor with Custom Controls that Support Predefined Values](xref:404599).
