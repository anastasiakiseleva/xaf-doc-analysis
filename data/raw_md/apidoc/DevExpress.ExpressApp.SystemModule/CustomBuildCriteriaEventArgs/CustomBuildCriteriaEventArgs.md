---
uid: DevExpress.ExpressApp.SystemModule.CustomBuildCriteriaEventArgs
name: CustomBuildCriteriaEventArgs
type: Class
summary: Arguments passed to the [FilterController.CustomBuildCriteria](xref:DevExpress.ExpressApp.SystemModule.FilterController.CustomBuildCriteria) event.
syntax:
  content: 'public class CustomBuildCriteriaEventArgs : HandledEventArgs'
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.CustomBuildCriteriaEventArgs._members
  altText: CustomBuildCriteriaEventArgs Members
---
The **CustomBuildCriteria** event allows you to create a custom **CriteriaOperator** that will be used by the **FullTextSearch** [Action](xref:112622) to filter a [List View](xref:112611). Since this event is triggered automatically by the [](xref:DevExpress.ExpressApp.SystemModule.FilterController), you do not need to instantiate **CustomBuildCriteriaEventArgs** objects.