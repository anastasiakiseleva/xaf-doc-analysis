---
uid: DevExpress.ExpressApp.ModuleBase.CustomizeTypesInfo(DevExpress.ExpressApp.DC.ITypesInfo)
name: CustomizeTypesInfo(ITypesInfo)
type: Method
summary: Customizes business class metadata before loading it to the [Application Model](xref:112580)'s **BOModel** node.
syntax:
  content: public virtual void CustomizeTypesInfo(ITypesInfo typesInfo)
  parameters:
  - id: typesInfo
    type: DevExpress.ExpressApp.DC.ITypesInfo
    description: An [](xref:DevExpress.ExpressApp.DC.ITypesInfo) object which holds metadata information on business classes to be loaded to the Application Model.
seealso:
- linkId: "113583"
---
When an XAF application is started, [the types info system](xref:113669) collects metadata information on the application's business classes. This metadata information is used to generate the BOModel node's child nodes and initialize their properties. The **CustomizeTypesInfo** method allows you to customize the collected metadata before it is used to generate the BOModel node. For instance, you can customize information which becomes read-only after the Application Model is generated. Additionally, you can add a custom class, member or attribute. To do this, override the **CustomizeTypesInfo** method and use the methods supplied by the types info system.

The following code snippet demonstrates how you can add members and attributes to existing business classes via the **CustomizeTypesInfo** method.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.DC;
using DevExpress.Persistent.Base;
//...
public sealed class MyModule : ModuleBase {
    //...
    public override void CustomizeTypesInfo(ITypesInfo typesInfo) {
        base.CustomizeTypesInfo(typesInfo);            
        ITypeInfo Department = XafTypesInfo.Instance.FindTypeInfo(typeof(Department));
        Department.CreateMember("Building", typeof(int));
        IMemberInfo DepartmentOffice = Department.FindMember("Office");
        DepartmentOffice.AddAttribute(new VisibleInReportsAttribute(false));          
    }
}
```
***

You can perform analogous actions via the [Controller.CustomizeTypesInfo](xref:DevExpress.ExpressApp.Controller.CustomizeTypesInfo(DevExpress.ExpressApp.DC.ITypesInfo)) method. It is more suitable when a feature that requires BOModel node customization is represented by a [Controller](xref:112621).