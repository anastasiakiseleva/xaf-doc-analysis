---
uid: DevExpress.Persistent.Base.VisibleInDashboardsAttribute
name: VisibleInDashboardsAttribute
type: Class
summary: When applied to a [business class](xref:113664), specifies whether end-users can create [dashboards](xref:117449) for objects of the attribute's target type. When applied to a business class property, specifies if the target property is visible in the Dashboard Designer.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Class | AttributeTargets.Property | AttributeTargets.Interface, Inherited = false)]
    public class VisibleInDashboardsAttribute : Attribute
seealso:
- linkId: DevExpress.Persistent.Base.VisibleInDashboardsAttribute._members
  altText: VisibleInDashboardsAttribute Members
---
When the `VisibleInDashboardsAttribute` attribute is applied to a business class, the corresponding item is added to the types list in the **Dashboards Data Source Wizard**. This allows users to create dashboards for objects of this class (see [Create, View and Modify Dashboards in a WinForms Application](xref:117450), [Create, View, and Modify Dashboards in an ASP.NET Core Blazor Application](xref:403400)).

**WinForms:**

![DashboardWinDataType](~/images/dashboardwindatatype125573.png)

When the `VisibleInDashboardsAttribute` attribute is applied to a business class property, and `false` is passed as a parameter, the target property is hidden from the Dashboard Designer.

