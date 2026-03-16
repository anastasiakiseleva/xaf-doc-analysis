---
uid: DevExpress.ExpressApp.SystemModule.IModelHiddenActions
name: IModelHiddenActions
type: Interface
summary: The HiddenActions node specifies Actions to be hidden when a View is displayed.
syntax:
  content: 'public interface IModelHiddenActions : IModelNode, IModelList<IModelActionLink>, IList<IModelActionLink>, ICollection<IModelActionLink>, IEnumerable<IModelActionLink>, IEnumerable'
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.IModelHiddenActions._members
  altText: IModelHiddenActions Members
- linkId: "112579"
- linkId: "112580"
---
The **IModelHiddenActions** node represents a list of the [](xref:DevExpress.ExpressApp.SystemModule.IModelActionLink) nodes. To hide an Action from the specific View, right-click the **Views** | **View** | **HiddenActions** node and choose **Add…** | **ActionLink**.

![HiddenActions_Create](~/images/hiddenactions_create117533.png)

Then, chose an Action to hide in the [IModelActionLink.Action](xref:DevExpress.ExpressApp.SystemModule.IModelActionLink.Action) property combo box.

![HiddenActions_ChooseAction](~/images/hiddenactions_chooseaction117532.png)

This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases. 