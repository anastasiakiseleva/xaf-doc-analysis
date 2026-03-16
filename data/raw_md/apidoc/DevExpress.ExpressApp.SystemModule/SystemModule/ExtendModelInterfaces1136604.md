---
uid: DevExpress.ExpressApp.SystemModule.SystemModule.ExtendModelInterfaces(DevExpress.ExpressApp.Model.ModelInterfaceExtenders)
name: ExtendModelInterfaces(ModelInterfaceExtenders)
type: Method
summary: Extends the [Application Model](xref:112580) with the [](xref:DevExpress.ExpressApp.SystemModule.IModelClassShowAutoFilterRow), [](xref:DevExpress.ExpressApp.SystemModule.IModelClassShowFindPanel), [](xref:DevExpress.ExpressApp.SystemModule.IModelListViewShowAutoFilterRow), and [](xref:DevExpress.ExpressApp.SystemModule.IModelListViewShowFindPanel) interfaces.
syntax:
  content: public override void ExtendModelInterfaces(ModelInterfaceExtenders extenders)
  parameters:
  - id: extenders
    type: DevExpress.ExpressApp.Model.ModelInterfaceExtenders
    description: A **ModelInterfaceExtenders** object representing a collection of Application Model interface extenders.
seealso:
- linkId: DevExpress.ExpressApp.IModelExtender
---
This method adds the [](xref:DevExpress.ExpressApp.Model.IModelClass) and **IModelClassDesignable** interfaces to the collection of extenders passed as the _extenders_ parameter.