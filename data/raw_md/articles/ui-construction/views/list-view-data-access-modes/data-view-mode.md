---
uid: "118452"
seealso: []
title: DataView Mode
owner: Ekaterina Kiseleva
---
# DataView Mode

## Mode Overview
The **DataView** mode improves [List View](xref:112611) performance by retrieving an [](xref:DevExpress.ExpressApp.XafDataView) lightweight read-only list of data records at once, instead of loading an [](xref:DevExpress.Xpo.XPCollection) or **DevExpress.ExpressApp.EFCore.EFCoreCollection** of persistent objects.

## Expected Behavior
* The [ListView.CurrentObject](xref:DevExpress.ExpressApp.ListView.CurrentObject), [ListView.SelectedObjects](xref:DevExpress.ExpressApp.ListView.SelectedObjects) and [SimpleActionExecuteEventArgs.SelectedObjects](xref:DevExpress.ExpressApp.Actions.SimpleActionExecuteEventArgs.SelectedObjects) properties return the [](xref:DevExpress.ExpressApp.Xpo.XpoDataViewRecord) or **DevExpress.ExpressApp.EFCore.EFCoreDataViewRecord** objects instead of original business objects. To get the real object, use the [IObjectSpace.GetObject](xref:DevExpress.ExpressApp.IObjectSpace.GetObject(System.Object)) method.
* Data for [non-persistent properties](xref:116516) does not show in List Views operating in **DataView** mode. However, [custom calculated fields](xref:113583) are correctly displayed in this mode if all properties referenced in [IModelMember.Expression](xref:DevExpress.ExpressApp.Model.IModelMember.Expression) are persistent.
* Inline editing is not supported in this mode. If an original object was modified, it does not display in a List View until you commit changes and reload the collection.
	
	For example, when an Action changes an object's property value, this object's instance is created by a separate database request and the property value's modification is not displayed on a grid until you commit changes (or it occurs automatically if the [BaseObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.BaseObjectSpace.CommitChanges) property is set to **true**).
	
	Also, if the Appearance and Security rules are applied to an object type in the current List View, and those criteria use objects' properties that are not contained in the [CollectionSourceBase.DisplayableProperties](xref:DevExpress.ExpressApp.CollectionSourceBase.DisplayableProperties) collection, these objects' instances are created by the separate database request to check each rule.
* Reference properties cannot be displayed in the **DataView** mode. The List Editor automatically replaces reference properties with their default nested properties (which can be defined using the [](xref:DevExpress.ExpressApp.DC.XafDefaultPropertyAttribute) attribute) when retrieving data. For instance, in the **Employee** List View, the **Employee.Department** property is replaced with **Employee.Department.Title**.
* The **DataView** mode is currently supported by the following built-in List Editors:
	- Windows Forms: [](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor), [](xref:DevExpress.ExpressApp.Scheduler.Win.SchedulerListEditor), [](xref:DevExpress.ExpressApp.PivotGrid.Win.PivotGridListEditor)
    - ASP.NET Core Blazor: [](xref:DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor), [](xref:DevExpress.ExpressApp.Blazor.Editors.DxChartListEditor)
* `SchedulerListEditor` does not support [Resources](xref:112813) in this mode.
* In nested List Views, the **Link**, **Unlink**, **New**, **Delete** and **Edit** Actions are disabled by design.
* The **OpenObjectController.OpenObject** Action is inactive in this mode.
* Using invisible properties in criteria evaluation is processed correctly, but it may have a negative performance impact because it leads to loading real objects through separate database requests. Using collection properties can cause much more recursive requests. 
	Consider using the [Client Mode](xref:118449) instead of **DataView** mode if you cannot avoid using such criteria because there is no difference in performance.

> [!NOTE]
> If you use the EF Core as your ORM system, implement Aggregated collections' cascade deletion as described in the **Cascade Deletion for Aggregated Entities** section of the [Relationships Between Entities in Code and UI](xref:402958) topic.
