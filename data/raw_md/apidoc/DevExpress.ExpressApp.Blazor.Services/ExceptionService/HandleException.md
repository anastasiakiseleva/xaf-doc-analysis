---
uid: DevExpress.ExpressApp.Blazor.Services.ExceptionService.HandleException(System.Exception)
name: HandleException(Exception)
type: Method
summary: Processes all XAF-handled exceptions if the [](xref:DevExpress.ExpressApp.Blazor.Services.ExceptionService) service is registered.
syntax:
  content: public virtual void HandleException(Exception exception)
  parameters:
  - id: exception
    type: System.Exception
    description: An exception to wrap.
seealso: []
---

> [!NOTE]
> For more information about the default error processing mechanism in XAF ASP.NET Core Blazor applications, refer to the following topic: [](xref:112704). 

XAF uses the [error boundary](https://learn.microsoft.com/en-us/aspnet/core/blazor/fundamentals/handle-errors#error-boundaries) mechanism to handle all exceptions except `IUserFriendlyException`. 

Override the `HandleException` method in the [](xref:DevExpress.ExpressApp.Blazor.Services.ExceptionService) class descendant to wrap an exception in a user-friendly exception (`IUserFriendlyException`).

For additional information, refer to the following class description: [](xref:DevExpress.ExpressApp.Blazor.Services.ExceptionService).