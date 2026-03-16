---
uid: DevExpress.Persistent.Base.EditorAliasAttribute
name: EditorAliasAttribute
type: Class
summary: Specifies the Property Editor alias.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Class | AttributeTargets.Property | AttributeTargets.Field, Inherited = true, AllowMultiple = false)]
    public class EditorAliasAttribute : Attribute
seealso:
- linkId: DevExpress.Persistent.Base.EditorAliasAttribute._members
  altText: EditorAliasAttribute Members
---
To assign a property editor to a specific business class' property, you can use the [IModelCommonMemberViewItem.PropertyEditorType](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.PropertyEditorType) property of the **BOModel** | **_\<Class\>_** | **OwnMembers** | **_\<Member\>_** node in the [Model Editor](xref:112582). Most Property Editors are platform-specific, and you cannot specify the editor type in the common module.

To assign an alias, you can use the [PropertyEditorAttribute](xref:DevExpress.ExpressApp.Editors.PropertyEditorAttribute.#ctor*) constructor that takes the _alias_ parameter.

# [C# (Blazor)](#tab/tabid-csharp-blazor)

```csharp
using DevExpress.ExpressApp.Editors;
using DevExpress.ExpressApp.Blazor.Editors;
// ...
[PropertyEditor(typeof(string), "MyStringPropertyEditorAlias", false)]
public class MyBlazorStringPropertyEditor : BlazorPropertyEditorBase {
    // ...
}
```

# [C# (WinForms)](#tab/tabid-csharp-win)

```csharp
using DevExpress.ExpressApp.Editors;
using DevExpress.ExpressApp.Win.Editors;
// ...
[PropertyEditor(typeof(string), "MyObjectPropertyEditorAlias", false)]
public class MyWinStringPropertyEditor : StringPropertyEditor {
    // ...
}
```
***

Now, you can pass`MyStringPropertyEditorAlias` to the `EditorAliasAttribute` to specify the property editor type of your business object in code without the use of the Model Editor.

If this attribute is applied to a property, then the property editor associated with the specified alias will be used for this property.

```csharp
[EditorAlias("MyStringPropertyEditorAlias")]
public string SimpleProperty { get; set; }
```

If this attribute is applied to a business class, then the property editor associated with the specified alias will be used for all [reference properties](xref:113572) of the target type.

```csharp
[EditorAlias("MyObjectPropertyEditorAlias")]
public class MyBusinessObject { 
    //...
}
```

> [!CAUTION]
> [!include[](~/templates/property-alias.md)]