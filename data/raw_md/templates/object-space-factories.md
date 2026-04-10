The `<:0:>` service allows you to use the DI-accessible API to create Object Spaces. 

In ASP.NET Core Blazor and Web API applications, `<:0:>` services use `IObjectSpaceProviderFactory` to create the collection of @DevExpress.ExpressApp.IObjectSpaceProvider objects. The [Template Kit](xref:405447) registers this service automatically.

The `<:0:>` service is the counterpart of the @DevExpress.ExpressApp.XafApplication.CreateObjectSpace(System.Type) method. The main difference between these techniques is that the service does not require an application instance. This improves your application performance but leads to the following restriction: 

* Customizations made in the application context (for example, in the [XafApplication.ObjectSpaceCreated](xref:DevExpress.ExpressApp.XafApplication.ObjectSpaceCreated) event handler) are ignored.

You can use the following Object Space Factories in different scenarios:

@DevExpress.ExpressApp.IObjectSpaceFactory
:   Creates Object Spaces for secured operations. In applications with the [Security System](xref:113366), it checks whether the current user is logged on. If the user is not logged on, it throws an authorization exception (refer to the following topic for information on how to avoid this exception: [Access Object Space, Security System, Caption Helper, and XAF Modules in the ASP.NET Core Environment](xref:403669)). Protected data is available depending on current user permissions. In applications without the Security System, this service operates the same way as `INonSecuredObjectSpaceFactory`.
@DevExpress.ExpressApp.INonSecuredObjectSpaceFactory
:   Creates Object Spaces for non-secured operations. These Object Spaces have full access to all objects and operations, regardless of user permission settings.
`IUpdatingObjectSpaceFactory`
:   Creates secured Object Spaces with additional permissions required for database update (for example, for new table creation). For more information, refer to the following method description: [IObjectSpaceProvider.CreateUpdatingObjectSpace](xref:DevExpress.ExpressApp.IObjectSpaceProvider.CreateUpdatingObjectSpace(System.Boolean)).