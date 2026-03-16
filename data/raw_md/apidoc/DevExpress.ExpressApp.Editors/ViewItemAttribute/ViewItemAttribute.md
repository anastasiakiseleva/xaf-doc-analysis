---
uid: DevExpress.ExpressApp.Editors.ViewItemAttribute
name: ViewItemAttribute
type: Class
summary: Applied to a custom [View Item](xref:112612). Registers the View Item in the application and specifies the type of the [Application Model](xref:112580)'s node used by the custom View Item.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Class, Inherited = true)]
    public class ViewItemAttribute : Attribute
seealso:
- linkId: DevExpress.ExpressApp.Editors.ViewItemAttribute._members
  altText: ViewItemAttribute Members
- linkId: DevExpress.ExpressApp.Editors.ViewItem
---
To use [a custom View Item](xref:405483) in the [Application Model](xref:112580) and [Views](xref:112611), decorate your custom View Item with the **ViewItemAttribute**. Pass a Model interface that extends the [](xref:DevExpress.ExpressApp.Model.IModelViewItem) interface or its descendant as the attribute's parameter. This interface defines the properties available in the Application Model. When the View Item is created, the corresponding model node is passed to its constructor via the model parameter:

# [C#](#tab/tabid-csharp)

```csharp
public MyDetailViewItem(IModelViewItem model, Type objectType) : base(objectType, model.Id) {
//...
```
***

This allows you to use the data from the corresponding Application Model's node, to initialize and configure the View Item.

The **ViewItemAttribute** attribute has several parameters. So, you have the following options:

* You want your View Item to be automatically set for the Application Model's nodes of a particular type. In this instance, pass the required node type as the attribute's parameter. Note that your View Item might not be used automatically as the default, if there is another View Item that uses this attribute with the same parameter.
* You implement an extra View Item for a particular data type, but you do not want it to be automatically set for the Application Model's nodes of this type. However, you need to be able to set it manually, when required. In this instance, pass the required node type as the first attribute parameter; and **false** as the second attribute parameter.

To see an example of using this attribute, refer to the [Implement Custom View Items](xref:405483) help topic.