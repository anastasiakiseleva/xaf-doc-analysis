---
uid: DevExpress.ExpressApp.SystemModule.RecordsNavigationController.OrderProviderSource
name: OrderProviderSource
type: Property
summary: Provides access to the **RecordsNavigationController**'s Order Provider.
syntax:
  content: public OrderProviderSource OrderProviderSource { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.SystemModule.OrderProviderSource
    description: An OrderProviderSource object representing a service for getting required objects from the specified View.
seealso: []
---
To determine what object collection to use, and how to get required objects from it, when the **NextObject** and **PreviousObject** Actions are executed, the **RecordsNavigationController** uses an **OrderProviderSource**. This object provides access to an **OrderProvider** object that has useful methods for implementing **NextObject** and **PreviousObject** Actions execution. There are several built-in Order Providers. In addition, you can implement a custom one. Use this property to set an **OrderProviderSource** with the required Order Provider for the **RecordsNavigationController**. For details, refer to the [](xref:DevExpress.ExpressApp.SystemModule.RecordsNavigationController) class description.