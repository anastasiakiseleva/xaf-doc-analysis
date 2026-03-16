---
uid: DevExpress.ExpressApp.SystemModule.LinkUnlinkController.CustomCreateLinkView
name: CustomCreateLinkView
type: Event
summary: Occurs when creating a View to be displayed by the [LinkUnlinkController.LinkAction](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController.LinkAction).
syntax:
  content: public event EventHandler<CustomCreateLinkViewEventArgs> CustomCreateLinkView
seealso:
- linkId: DevExpress.ExpressApp.XafApplication.CreateListView*
---
Handle this event to create a custom View that will be displayed when executing the **Link** Action. While creating a custom View, use the event handler's **CustomCreateLinkViewEventArgs.SourceView** parameter, to get the nested View from which the **LinkUnlinkController** has activated. Set the handler's **CustomCreateLinkViewEventArgs.LinkView** to the custom View created. To prevent the creation of the default Link View, set the handler's **CustomCreateLinkViewEventArgs.Handled** parameter to **true**.