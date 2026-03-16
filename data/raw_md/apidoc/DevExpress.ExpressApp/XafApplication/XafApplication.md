---
uid: DevExpress.ExpressApp.XafApplication
name: XafApplication
type: Class
summary: Manages an XAF application.
syntax:
  content: 'public abstract class XafApplication : Component, INotifyPropertyChanged, ISupportInitialize, IApplicationModelManagerProvider, IInternalCollectionSourceCreating, IAsyncDisposable'
seealso:
- linkId: DevExpress.ExpressApp.XafApplication._members
  altText: XafApplication Members
---
The `XafApplication` class contains methods to create [Controllers](xref:112621), [Views](xref:112611), Object Space (see [](xref:DevExpress.ExpressApp.BaseObjectSpace)), and other XAF elements. Its properties specify application name and title, configuration string, provide access to the [Application Model](xref:112580), modules and the strategy that manages View visibility. You can customize many built-in mechanisms to manage your application. For this purpose, use `XafApplication`'s events.

XAF creates and initializes a `XafApplication` descendant as follows:

Platform | Created and Initialized | File
---|---|---
ASP.NET Core Blazor | When `IXafApplicationProvider.GetApplication()` is called for the first time (usually when XAF initializes the page). | _Startup.cs_
Windows Forms | In the `Main` method. | _Program.cs_
[Application Server](xref:113439) | In the `ApplicationServerService` constructor. | _ApplicationServerService.cs_
[](xref:403394) | Only during initialization. | _Startup.cs_

> [!NOTE]
> `XafApplication` is not available in Web API Service endpoints. XAF creates it on service initialization only for [compatibility check](xref:DevExpress.ExpressApp.XafApplication.CheckCompatibility) and localization services setup.

## Usage Considerations

`XafApplication` is essential for an application's initial setup (for example, to set up modules and gather `TypesInfo`). However, after this initial setup, some services can function independently of `XafApplication`. We recommend that you use the APIs provided by these services instead of the `XafApplication` API for the same tasks because events and methods within `XafApplication` may not trigger if the corresponding operation occurs outside its context.

For example, if you subscribe to the [XafApplication.ObjectSpaceCreated](xref:DevExpress.ExpressApp.XafApplication.ObjectSpaceCreated) event, it is not guaranteed to fire because it is possible to create `IObjectSpace` outside of `XafApplication`. To handle occurrences when an `IObjectSpace` is created use the [ObjectSpaceProviderEvents.OnObjectSpaceCreated](xref:DevExpress.ExpressApp.ObjectSpaceProviderEvents.OnObjectSpaceCreated) method.

As another important example, you need to keep in mind that the [XafApplication.LoggedOn](xref:DevExpress.ExpressApp.XafApplication.LoggedOn) does not fire every time that a user is logged in by the Security System. For instance, the event does not fire in the following cases:

- When a request to load data for a [Dashboard](xref:117449) or [Report](xref:113591) is processed.
- When [Web API Service](xref:403394) handles a request, it disposes of its `XafApplication` instance after the initial setup is completed. After that, you can only use services. See the following topic for information on how to access these services: [](xref:403861).

For more information and examples, refer to the following ticket: [Core - ValueManager API availability and deprecated static helpers in XAF .NET 6+ apps (Blazor, Web API Service, WinForms)](https://supportcenter.devexpress.com/ticket/details/t1121273/core-valuemanager-api-availability-and-deprecated-static-helpers-in-xaf-net-6-apps).




