---
uid: DevExpress.Persistent.Base.ImmediatePostDataAttribute
name: ImmediatePostDataAttribute
type: Class
summary: An attribute you can apply to business class properties. This attribute indicates that the Property Editor's control value should be passed to the property of a bound object as soon as possible when a user changes the editor's value.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Property, Inherited = true, AllowMultiple = false)]
    public sealed class ImmediatePostDataAttribute : ModelExportedValueAttribute
seealso:
- linkId: DevExpress.Persistent.Base.ImmediatePostDataAttribute._members
  altText: ImmediatePostDataAttribute Members
- linkId: DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.ImmediatePostData
---
The following code snippet applies the `ImmediatePostData` attribute to a business class property. For example, this property allows you to force an update of other values that are calculated based on the current property.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.Persistent.Base;
// ...
[ImmediatePostData]
public double Rate {
    get {
        //...
    }
    set {
        //...           
    }
}
```
***

### Impact on Other Properties

When you apply the `ImmediatePostData` attribute to a business class property, you automatically set the [Application Model](xref:112580)'s **BOModel** | **_\<Class\>_** | **OwnMembers** | **_\<Member\>_** | **ImmediatePostData** default property value to `true`.

![ImmediatePostData_ApplicationModel_BOModel](~/images/immediatepostdata_applicationmodel_bomodel131595.png)

Note that you can set or change this property's value using the [Model Editor](xref:112582) as shown in the [Make a Property Calculable](xref:404195) topic.

Any changes to the **BOModel** | **_\<Class\>_** | **OwnMembers** | **_\<Member\>_** | **ImmediatePostData** property value affect the default value of the same property in the following nodes:

* [!include[Node_Views_DetailView_Items_PropertyEditor](~/templates/node_views_detailview_items_propertyeditor111384.md)],
* [!include[Node_Views_ListView_Columns_Column](~/templates/node_views_listview_columns_column111388.md)].

You can modify the property's value in the nodes above to, for example, disable `ImmediatePostData` for certain Views.

![ImmediatePostData_ApplicationModel_Views](~/images/immediatepostdata_applicationmodel_views131596.png)

These nodes' `ImmediatePostData` properties specify the default values for the corresponding [PropertyEditor.ImmediatePostData](xref:DevExpress.ExpressApp.Editors.PropertyEditor.ImmediatePostData) properties.

The diagram below demonstrates different levels where the `ImmediatePostData` setting can be applied. Higher levels determine default values for lower levels.

![ImmediatePostData_Class](~/images/immediatepostdata_class131622.png)

### Limitations

* In [Batch edit mode](xref:113249#in-place-editing-customization-the-inlineeditmode-property), `ImmediatePostData` affects properties of the current row only.
