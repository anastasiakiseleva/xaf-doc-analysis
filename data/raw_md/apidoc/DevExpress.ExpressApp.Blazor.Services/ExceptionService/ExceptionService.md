---
uid: DevExpress.ExpressApp.Blazor.Services.ExceptionService
name: ExceptionService
type: Class
summary: A service that allows you to handle exceptions in a custom manner.
syntax:
  content: 'public class ExceptionService : IExceptionHandlerService, IExceptionProviderService'
seealso:
- linkId: DevExpress.ExpressApp.Blazor.Services.ExceptionService._members
  altText: ExceptionService Members
---

> [!NOTE]
> For more information about the default error processing mechanism in XAF ASP.NET Core Blazor applications, refer to the following topic: [](xref:112704). 

Override the [ExceptionService.HandleException(Exception)](xref:DevExpress.ExpressApp.Blazor.Services.ExceptionService.HandleException(System.Exception)) method in the class descendant to wrap an exception in a user-friendly exception.

Override the [ExceptionService.ShouldHandleException(Exception)](xref:DevExpress.ExpressApp.Blazor.Services.ExceptionService.ShouldHandleException(System.Exception)) method in the class descendant to determine how you want to process exceptions.

The following example displays a user-friendly exception message in your XAF Blazor UI application:

1. Add a controller:

    # [C#](#tab/tabid-csharp1)
    
    ```csharp
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Actions;
    using System;

    namespace MySolution.Module.Controllers {
        public class MyTestException : Exception {
        }

        public partial class TestExceptionController : ViewController {
            public TestExceptionController() {
                // When a user clicks this action, an exception is thrown.
                SimpleAction simpleAction = new SimpleAction(this, "Test Action", DevExpress.Persistent.Base.PredefinedCategory.Edit);
                simpleAction.Execute += SimpleAction_Execute;
            }

            private void SimpleAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
                throw new MyTestException();
            }
        }
    }
    ```
    ***

2. Add a `MyTestExceptionService` service and override the [HandleException](xref:DevExpress.ExpressApp.Blazor.Services.ExceptionService.HandleException(System.Exception)) method:

    # [C#](#tab/tabid-csharp1)
    
    ```csharp{3-6}
    public class MyTestExceptionService : ExceptionService {
        public MyTestExceptionService(ILogger<ExceptionService> logger) : base(logger) { }
        public override bool ShouldHandleException(Exception exception) {
            if(exception is MyTestException) {
                return true;
            }
            else {
                return false;
            }
        }
        public override void HandleException(Exception exception) {
            Exception result = exception is MyTestException ? new UserFriendlyException("My Test User Friendly Exception", exception) : exception;
            base.HandleException(result);
        }
    }
    ```
    ***

3. Register the `MyTestExceptionService` service in the `MySolution.Blazor.Server\Startup.cs` file: 

    # [C#](#tab/tabid-csharp1)
    
    ```csharp{3-4}
    // ...
    services.AddXaf<MySolutionBlazorApplication>(Configuration);
    // Register the service.
    services.AddScoped<IExceptionHandlerService, MyTestExceptionService>();
    // ...
    ```
    ***

4. Run the application and click the **Test Action** button. The user-friendly exception is displayed within a toast notification.

    ![xaf blazor user friendly url](~/images/blazor-user-friendly-url.gif)