---
uid: DevExpress.Persistent.Base.DefaultClassOptionsAttribute
name: DefaultClassOptionsAttribute
type: Class
summary: Sets default options for a class.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Class | AttributeTargets.Interface, Inherited = false)]
    public class DefaultClassOptionsAttribute : Attribute
seealso:
- linkId: DevExpress.Persistent.Base.DefaultClassOptionsAttribute._members
  altText: DefaultClassOptionsAttribute Members
- linkId: "112701"
---
The following default options are set when you apply `DefaultClassOptionsAttribute` to a business class:

* The corresponding item is added to the navigation control's Default navigation item. This allows users to display a View with objects of this class.
* The corresponding item is added to the **New** Action's Items list. This allows users to create objects of this class when objects of another type are displayed in the View.
* The corresponding item is added to the **Data Type** drop-down list in the Report Wizard. This allows users to create reports for objects of this class. For more information about how you can create and view reports in an XAF application, refer to the following topics:
  * [](xref:402306)
  * [](xref:113646) 
* The corresponding item is added to the type list in the Dashboards Data Source Wizard. This allows users to create [dashboards](xref:117449) for objects of this class. For more information about how you can create, view, and modify Dashboards, refer to the following topics:
  * [](xref:403400)
  * [](xref:117450) 

If you do not want to set all the options specified above at the same time, use the following attributes:
* [](xref:DevExpress.Persistent.Base.CreatableItemAttribute)
* [](xref:DevExpress.Persistent.Base.NavigationItemAttribute)
* [](xref:DevExpress.Persistent.Base.VisibleInReportsAttribute)
* [](xref:DevExpress.Persistent.Base.VisibleInDashboardsAttribute).