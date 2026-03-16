---
uid: DevExpress.ExpressApp.SystemModule.IModelPropertyEditorLinkView.LinkView
name: LinkView
type: Property
summary: Specifies the View invoked by the [LinkUnlinkController.LinkAction](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController.LinkAction).
syntax:
  content: |-
    [DataSourceProperty("LinkViews", new string[]{})]
    [ModelBrowsable(typeof(LinkViewCalculator))]
    IModelListView LinkView { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Model.IModelListView
    description: An [](xref:DevExpress.ExpressApp.Model.IModelListView) object representing a ListView node which corresponds to the List View invoked by the **Link** Action.
seealso: []
---
