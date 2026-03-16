---
uid: DevExpress.ExpressApp.Model.IModelApplication
name: IModelApplication
type: Interface
summary: Properties of the Application node provide general information on the current application.
syntax:
  content: |-
    [DisplayProperty("Title")]
    [ImageName("ModelEditor_Application")]
    public interface IModelApplication : IModelNode
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelApplication._members
  altText: IModelApplication Members
- linkId: "112579"
---
This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases.

> [!NOTE]
> Use the following properties values to form the application's About information:  
> * [IModelApplication.Company](xref:DevExpress.ExpressApp.Model.IModelApplication.Company)
> * [IModelApplication.Copyright](xref:DevExpress.ExpressApp.Model.IModelApplication.Copyright)
> * [IModelApplication.Description](xref:DevExpress.ExpressApp.Model.IModelApplication.Description)
> * [IModelApplication.VersionFormat](xref:DevExpress.ExpressApp.Model.IModelApplication.VersionFormat),
> * [IModelApplication.Title](xref:DevExpress.ExpressApp.Model.IModelApplication.Title)
> * [IModelApplication.Logo](xref:DevExpress.ExpressApp.Model.IModelApplication.Logo)
>
> Refer to the following topic for additional information: [Application Icon, Logo & About Info](xref:113445).