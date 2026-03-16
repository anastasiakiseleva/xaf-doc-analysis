---
uid: DevExpress.ExpressApp.Scheduler.ResourceDataSourceCreatingEventArgs
name: ResourceDataSourceCreatingEventArgs
type: Class
summary: Represents arguments passed to the [SchedulerListEditorBase.ResourceDataSourceCreating](xref:DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase.ResourceDataSourceCreating) event.
syntax:
  content: 'public class ResourceDataSourceCreatingEventArgs : HandledEventArgs'
seealso:
- linkId: DevExpress.ExpressApp.Scheduler.ResourceDataSourceCreatingEventArgs._members
  altText: ResourceDataSourceCreatingEventArgs Members
---
The **ResourceDataSourceCreating** event is raised in the protected [](xref:DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase).**CreateResourcesDataSource** method. You can use the **ResourceDataSourceCreating** event to specify a custom resources data source to be used by the **SchedulerListEditorBase**'s descendant. The handler's [ResourceDataSourceCreatingEventArgs.ResourceType](xref:DevExpress.ExpressApp.Scheduler.ResourceDataSourceCreatingEventArgs.ResourceType) parameter specifies the type of resource objects used by the scheduling control. Instantiate a collection of the required resources and pass it to the handler's [ResourceDataSourceCreatingEventArgs.DataSource](xref:DevExpress.ExpressApp.Scheduler.ResourceDataSourceCreatingEventArgs.DataSource) parameter. Set the handler's **Handled** parameter to **true**, to prohibit the creation of the default resources collection.

To perform custom actions over the resources data source used by the **SchedulerListEditorBase**'s descendant, handle the [SchedulerListEditorBase.ResourceDataSourceCreated](xref:DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase.ResourceDataSourceCreated).

For information on resources, refer to the [Resources in a Schedule](xref:112813) topic.