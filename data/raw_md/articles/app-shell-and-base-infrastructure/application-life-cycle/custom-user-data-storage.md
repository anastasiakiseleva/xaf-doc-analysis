---
uid: "405895"
title: Storage of Global Application Settings and User Data
---
# Storage of Global Application Settings and User Data

An XAF application stores application-wide options and user-specific data in the [Application Model](xref:112580). You can switch to other storage types and choose either persistent or non-persistent options, depending on your needs.

- Choose **persistent storage** to save options across application restarts.
- Choose **non-persistent storage** to keep options only while the application or view is running.

This topic lists available data storage options for XAF applications.

## Database

_Persistent Storage_

Create a dedicated database table to store your settings. Access the table through the same ORM layer (XPO or EF Core) that your XAF application uses.

Use this approach to share settings across application instances or between users, and need to edit them through a standard XAF Detail View.

You can find more information about this approach in the following help topics: 

* <xref:112916>
* <xref:113698>

## File System or External Disk Storage

_Persistent Storage_

Store settings in XML or JSON files, or any file-based format on a local or network disk. This approach works independently of XAF and uses standard .NET practices.

XAF ships with the [File Attachments](xref:112781) module (and @DevExpress.Persistent.Base.IFileData as part of it), which helps you link ORM business classes to a file system or any other storage (like Dropbox or any other Cloud storage).

## Application Model

_Persistent Storage_

The [Application Model](xref:112580) is XAF's default storage for UI settings and per-user customizations. You can [extend the Application Model](xref:112785) with custom nodes and attributes to store your options alongside built-in settings. 

Refer to the following topic to learn how to access data from the application model: [Read and Set Values for Built-in Application Model Nodes in Code](xref:112810).


## Memory of the Current Process

_Non-Persistent Storage_

Create classes with static or instance variables whose lifetime matches the scope. The implementation differs by application type. A WinForms desktop client manages state differently from a multi-user ASP.NET server application. See [MSDN](https://learn.microsoft.com) and [Stack Overflow](https://stackoverflow.com) for general guidance on in-process state management.

* To store custom data during **a certain View lifetime**, create a @DevExpress.ExpressApp.ViewController with non-static variables. The Controller is disposed of when the View is closed. Use the @DevExpress.ExpressApp.Frame.GetController``1 method to access the Controller.
* To hold custom data during **the entire application lifetime**, create a variable at the Application level.

You can also use any XAF or non-XAF class whose lifetime matches your needs as in-memory data storage.

## Custom ASP.NET Core Service

_Non-Persistent Storage_

In ASP.NET Core-based XAF applications, create custom services and register them in the `ConfigureServices` method in the _Startup.cs_ file.

**File**: _SolutionName.Blazor.Server\Startup.cs_, _SolutionName.WebApi\Startup.cs_

````csharp
public class Startup {
    public void ConfigureServices(IServiceCollection services) {
    // Register a scoped service (per-user session)
    services.AddScoped<IMySettingsService, MySettingsService>();
    // Register a singleton service (application-wide)
    services.AddSingleton<IGlobalConfigService, GlobalConfigService>();
    // ...
````

### Example: How to Define the Connection String Based on the User

1. Create a service that stores user name and connection string in a dictionary:

    ```csharp
    public class MyUserCSService {
        Dictionary<string, string> store;
        public MyUserCSService() {
            store = new Dictionary<string, string>();
        }
        public void AddCS(string userName, string cs) {
            if (!store.ContainsKey(userName)) {
                store.Add(userName, cs);
            }
        }
        public string GetCS(string userName) {
            string cs;
            store.TryGetValue(userName, out cs);
            return cs;
        }
    }
    ```

2. Register this service in the `ConfigureServices` method:

    ```csharp
    public class Startup {
        public void ConfigureServices(IServiceCollection services) {
            services.AddSingleton<MyUserCSService>();
            //...
    ```

3. After this, you can get the user connection string or add a new user connection string in the following way:

    ```csharp
    // add
    MyUserCSService myService = ServiceProvider.GetRequiredService<MyUserCSService>();
    myService.AddCS(userName, "CS");

    // get
    MyUserCSService myService = ServiceProvider.GetRequiredService<MyUserCSService>();
    string cs = myService.GetCS(username);
    ```

## Other Approaches

You can use standard solutions from Microsoft documentation: [Session and state management in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/app-state).

## Common Considerations

* You cannot use the legacy ValueManager API in XAF Blazor UI, Web API Service, and other non-XAF UI apps. For additional information, refer to the following breaking change article: [Core - InvalidOperationException (ValueManagerContext.Storage is null) may occur in XAF Blazor, Web API Service, and other non-XAF UI apps](https://supportcenter.devexpress.com/ticket/details/t1121273/core-valuemanager-api-availability-and-deprecated-static-helpers-in-xaf-net-6-apps).


* Do not reference application settings (like Application Model values) directly in persistent business class code. Keep the data model layer independent from how application settings are stored and retrieved.

    **Reasons:**

    - Business objects do not have access to the Application Model or other UI-layer services at the ORM level.
    - The same data model can be reused across multiple applications that may store settings differently.

    The only exception is when settings are part of the data model itself (for instance, you implemented a persistent Singleton class).

    Instead, use the business logic layer. Controllers act as the bridge between the UI and the data model. The following code shows how a `ViewController` tracks new data records and assigns a default currency to new business objects based on current application settings:

    ```csharp
    protected override void OnActivated() {
            base.OnActivated();
            if (View.CurrentObject is Invoice invoice && ObjectSpace.IsNewObject(invoice)) {
                // Assign a default value from application settings.
                invoice.Currency = GetDefaultCurrencyFromSettings();
            }
    }
    ```