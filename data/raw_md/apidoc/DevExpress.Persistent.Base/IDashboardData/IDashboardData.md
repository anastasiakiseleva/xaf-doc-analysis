---
uid: DevExpress.Persistent.Base.IDashboardData
name: IDashboardData
type: Interface
summary: Declares members of the persistent classes used by the [Dashboards Module](xref:117449) to store dashboards in the application database.
syntax:
  content: public interface IDashboardData
seealso:
- linkId: DevExpress.Persistent.Base.IDashboardData._members
  altText: IDashboardData Members
---
Built-in implementations of **IDashboardData** are the [](xref:DevExpress.Persistent.BaseImpl.DashboardData) XPO persistent class and [](xref:DevExpress.Persistent.BaseImpl.EF.DashboardData) Entity Framework class.

If you have created a custom class that supports  **IDashboardData**, pass the implemented type to the [DashboardsModule.DashboardDataType](xref:DevExpress.ExpressApp.Dashboards.DashboardsModule.DashboardDataType) property to use it instead of the default implementation.