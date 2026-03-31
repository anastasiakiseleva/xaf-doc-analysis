---
uid: "112813"
seealso: []
title: Resources in a Schedule
---
# Resources in a Schedule

This topic introduces the concept of the [Resources](xref:1756) feature supported by the [Scheduler Module](xref:112812), describes how scheduler events and resources are associated, and details how resources can be assigned to scheduler events.

## What is a Resource?

In real-life scheduling applications where one deals with a large amount of data that needs to be scheduled, appointments (scheduler events) are seldom processed "as is", and are usually assigned to different resources. Resources can be of different kinds, and the decision as to what should be a resource in a particular scheduling application depends on the specifics of the task performed by that application. The following are examples of scheduling tasks that illustrate what can be an appointment and a resource in these tasks.

* _A Company_.
	
	Resource: Every employee in this company
	
	Event: Any time interval which is spent by an employee to perform a particular task.
* _A Car Rental Agency_.
	
	Resource: Every car which is owned by this firm and available for rental.
	
	Event: Any time interval when any of the firm's cars are rented.
* _An Educational Center_.
	
	Resources: Every teacher who works at this center, or every classroom in this center.
	
	Event: Any time interval when any of the teachers are delivering a lecture in any of the classrooms in the center.
	> [!NOTE]
	> This last example, may come with two possible kinds of resources (teachers and rooms). However, the Scheduler controls do not allow events to belong to resources of a different types. So, to display this data in a scheduling application, we suggest you use two different Event List Views. One Event List View may be used to display teachers as resources, and another Event List View may be used to display rooms as resources. Both, however, should be bound to the same data to ensure consistency.

## Association Between Resources and Scheduler Events

The Scheduler module works with classes that implement the `DevExpress.Persistent.Base.General.IEvent` interface and those that implement the `DevExpress.Persistent.Base.General.IResource` interface. To support the Resources feature, the `IEvent` interface exposes the `ResourceId` property. This property specifies an XML string that lists the identifiers of associated resources. In Windows Forms applications, the Scheduler module supports the **ResourceSharing** strategy where several Resources can be assigned to an Event. The following image demonstrates this concept:

![Resources_Sharing](~/images/resources_sharing115592.png)

The built-in `DevExpress.Persistent.BaseImpl.Event` class, which implements the `IEvent` interface, has a Many-to-Many association with the built-in `DevExpress.Persistent.BaseImpl.Resource` class, which implements the `IResource` interface. All Resource objects from the Event's `Resources` collection are listed in the Event's `IEvent.ResourceId` property.

## Use Built-in Event and Resource Classes

To use the built-in `Event` and `Resource` classes in your application, add the `Event` class to a module in your solution as described in the following topic: [](xref:112847#import-classes-from-a-business-class-library-or-module). The built-in `Resource` class is added automatically with the `Event` class. If you use the `DevExpress.Persistent.BaseImpl.EF.Event` (Entity Framework Core) or `DevExpress.Persistent.BaseImpl.Event` (XPO) class' descendant, the built-in `DevExpress.Persistent.BaseImpl.EF.Resource` (Entity Framework Core) or `DevExpress.Persistent.BaseImpl.Resource` (XPO) class is also added to the process of automatic UI generation. This allows you to have an extended `Event` class, but use the inherited association with the `Resource` class.

At runtime, you can create and display `Resource` objects by displaying the Resource List View and Detail View. In addition, you can add the required resources to an Event's `Resources` collection in the Event Detail View:

ASP.NET Core Blazor
:   ![Resources in Event Detail View, ASP.NET Core Blazor, DevExpress](~/images/resources-in-event-detail-view-blazor-devexpress.png)

Windows Forms
:   ![|Resources in Event Detail View, Windows Forms, DevExpress|](~/images/resources_eventdetailview_win115961.png)

Resources are also displayed in Event List Views. The following image shows how a collection of two Resources (1 and 2) is displayed in an Event List View:

ASp.NET Core Blazor
:   ![|Resources in Event List View, ASP.NET Core Blazor, DevExpress|](~/images/resources-in-event-list-view-blazor-devexpress.png)

Windows Forms
:   ![|Resources in Event List View, Windows Forms, DevExpress|](~/images/resources_eventlistview115964.png)

In Windows Forms applications, use the [Resource Navigator](xref:2137) at the bottom right area of the Scheduler Control to scroll through resources and change the number of resources displayed at one time on the screen.

## Use a Custom Resource Class

To be supported by the Scheduler module, a `Resource` class must implement the `DevExpress.Persistent.Base.General.IResource` interface. The built-in `DevExpress.Persistent.BaseImpl.EF.Resource` (Entity Framework Core) and `DevExpress.Persistent.BaseImpl.Resource` (XPO) class from the [Business Class Library](xref:112571) implements this interface. A custom `Resource` class must implement this interface as well. To implement a custom `Resource` class, inherit from the built-in `Resource` class or implement the `IResource` interface from scratch. You can find the sources of the built-in Resource class at the following location:
* Entity Framework Core: _[!include[PathToXafInstallation](~/templates/path-to-installation.md)]Sources\DevExpress.Persistent\DevExpress.Persistent.BaseImpl.EFCore\Resource.cs_
* XPO: _[!include[PathToXafInstallation](~/templates/path-to-installation.md)]Sources\DevExpress.Persistent\DevExpress.Persistent.BaseImpl.Xpo\Resource.cs_

Since the built-in `Event` class is associated with the built-in `Resource` class, you have to implement a custom `Event` class to associate it with the custom `Resource` class. For this purpose, use the sources of the built-in `Event` class. You can find them at the following location:
* Entity Framework Core: _[!include[PathToXafInstallation](~/templates/path-to-installation.md)]Sources\DevExpress.Persistent\DevExpress.Persistent.BaseImpl.EFCore\Event.cs_
* XPO: _[!include[PathToXafInstallation](~/templates/path-to-installation.md)]Sources\DevExpress.Persistent\DevExpress.Persistent.BaseImpl.Xpo\Event.cs_

The type of objects that serve as a resource data source for the Scheduler [List Editor](xref:113189) must be set to the [IModelListViewScheduler.ResourceClass](xref:DevExpress.ExpressApp.Scheduler.IModelListViewScheduler.ResourceClass) property of the [Application Model](xref:112580)'s [!include[Node_Views_ListView](~/templates/node_views_listview111381.md)] node:

![ResourceClassName](~/images/resourceclass116236.png)

The Application Model is extended with this property by the Scheduler module. If you have a single class that implements the `IResource` interface in your application, this class is assigned to this property automatically. If you have several classes that implement the `IResource` interface, you can assign any of them to this property. Otherwise, XAF selects the first found type.

> [!TIP]
> For more information on how to implement a custom resource class, refer to the following example: [XAF - Create Custom Event and Resource Classes for XAF Scheduler](https://github.com/DevExpress-Examples/xaf-how-to-create-custom-event-and-resource-classes-for-scheduler)

## Filter Resources in Scheduler

Use the `SchedulerListEditorBase.ResourceDataSourceCreating` event to create and filter a resources data source.

# [Entity Framework Core](#tab/tabid-csharp-efcore)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Scheduler;
using DevExpress.Persistent.Base.General;
using DevExpress.Xpo.DB;
using DevExpress.Xpo;
using DevExpress.Data.Filtering;
using DevExpress.Persistent.BaseImpl.EF;

namespace YourApplicationName.Blazor.Server.Controllers;

public class FilterResourcesController : ObjectViewController<ListView, IEvent> {
    protected override void OnActivated() {
        base.OnActivated();
        SchedulerListEditorBase editor = (SchedulerListEditorBase)View.Editor;
        editor.ResourceDataSourceCreating += Editor_ResourceDataSourceCreating;
    }
    protected override void OnDeactivated() {
        base.OnDeactivated();
        SchedulerListEditorBase editor = (SchedulerListEditorBase)View.Editor;
        editor.ResourceDataSourceCreating -= Editor_ResourceDataSourceCreating;
    }
    private void Editor_ResourceDataSourceCreating(object sender, ResourceDataSourceCreatingEventArgs e) {
        var filterCriteria = CriteriaOperator.FromLambda<IResource>(x => x.Caption == "Resource1");
        var sortProperties = new[] { new SortProperty(nameof(IResource.Caption), SortingDirection.Ascending) };
        e.DataSource = ObjectSpace.CreateCollection(typeof(Resource), filterCriteria, sortProperties);
        e.Handled = true;
    }
}
```

# [XPO](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.ExpressApp.Scheduler;
using DevExpress.ExpressApp;
using DevExpress.Persistent.Base.General;
using DevExpress.Data.Filtering;
using DevExpress.Xpo;
using DevExpress.Xpo.DB;

namespace YourApplicationName.Blazor.Server.Controllers;

public class FilterResourcesController :ObjectViewController<ListView, IEvent> {
    protected override void OnActivated() {
        base.OnActivated();
        SchedulerListEditorBase editor = (SchedulerListEditorBase)View.Editor;
        editor.ResourceDataSourceCreating += Editor_ResourceDataSourceCreating;
    }
    protected override void OnDeactivated() {
        base.OnDeactivated();
        SchedulerListEditorBase editor = (SchedulerListEditorBase)View.Editor;
        editor.ResourceDataSourceCreating -= Editor_ResourceDataSourceCreating;
    }
    private void Editor_ResourceDataSourceCreating(object sender, ResourceDataSourceCreatingEventArgs e) {
        var filterCriteria = CriteriaOperator.FromLambda<IResource>(x => x.Caption == "Resource1");
        var sortProperties = new[] { new SortProperty(nameof(IResource.Caption), SortingDirection.Ascending) };
        e.DataSource = ObjectSpace.CreateCollection(typeof(DevExpress.Persistent.BaseImpl.Resource), filterCriteria);
        e.Handled = true;
    }
}
```
***

Use the `SchedulerListEditorBase.ResourceDataSourceCreated` event to filter the existing resources data source.

# [C#](#tab/tabid-csharp)
```csharp
using DevExpress.ExpressApp.Scheduler;
using DevExpress.ExpressApp;
using DevExpress.Persistent.Base.General;
using DevExpress.Data.Filtering;

namespace YourApplicationName.Blazor.Server.Controllers;

public class FilterResourcesController : ObjectViewController<ListView, IEvent> {
    protected override void OnActivated() {
        base.OnActivated();
        SchedulerListEditorBase editor = (SchedulerListEditorBase)View.Editor;
        editor.ResourceDataSourceCreated += Editor_ResourceDataSourceCreated;
    }
    protected override void OnDeactivated() {
        base.OnDeactivated();
        SchedulerListEditorBase editor = (SchedulerListEditorBase)View.Editor;
        editor.ResourceDataSourceCreated -= Editor_ResourceDataSourceCreated;
    }
    private void Editor_ResourceDataSourceCreated(Object sender, ResourceDataSourceCreatedEventArgs e) {
        var resourcesDataSource = e.DataSource;
        var filterCriteria = CriteriaOperator.FromLambda<IResource>(x => x.Caption == "Resource1");
        ObjectSpace.ApplyCriteria(resourcesDataSource, filterCriteria);
    }
}
```
***
