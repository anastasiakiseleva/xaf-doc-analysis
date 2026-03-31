---
uid: "404430"
title: Register Services in the Dependency Injection Container
seealso:
  - linkId: '405025'
---
# Register Services in the Dependency Injection Container

Register services required for your Controller in the dependency injection container. For this purpose, use @Microsoft.Extensions.DependencyInjection.IServiceCollection.

ASP.NET Core Blazor
:   Use the `services` parameter of the `Startup.ConfigureServices` method in the _YourApplicationName.Blazor.Server\Startup.cs_ file:
   
    ```csharp
    public void ConfigureServices(IServiceCollection services) { 
    //... 
      services.AddSingleton<IServiceOne, ConcreteServiceOne>(); 
      services.AddTransient<IServiceTwo, ConcreteServiceTwo>(); 
    //...
    } 
    ```
Windows Forms
:   To access the collection, use the [Services](xref:DevExpress.ExpressApp.ApplicationBuilder.IXafApplicationBuilder`1.Services) property of the application builder object. The [WinApplication.CreateBuilder](xref:DevExpress.ExpressApp.Win.WinApplication.CreateBuilder(System.Action{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilderOptions})) method creates this object in the _YourApplicationName.Win\Startup.cs_ file:

    ```csharp
    var builder = WinApplication.CreateBuilder(); 
    builder.Services.AddSingleton<IServiceOne, ConcreteServiceOne>(); 
    builder.Services.AddTransient<IServiceTwo, ConcreteServiceTwo>(); 
    ```
## Access Services Using XafApplication

You can use [XafApplication.ServiceProvider](xref:DevExpress.ExpressApp.XafApplication.ServiceProvider) property to obtain services from a built-in service container. The following code sample demonstrates how to access [](xref:DevExpress.ExpressApp.Services.Localization.ICaptionHelperProvider):

```csharp
public class YourViewController : ViewController {
    protected override void OnActivated() {
        base.OnActivated();
        var caption = Application.ServiceProvider.GetService<ICaptionHelperProvider>().GetCaptionHelper().GetActionCaption("SaveAndNew");
    }
}
```
[`Application.ServiceProvider`]: xref:DevExpress.ExpressApp.XafApplication.ServiceProvider

For information about access to services in Business Objects, refer to the following topic: [](xref:404403).

## Dependency Injection with Third-party Inversion of Control (IoC) Service Containers

In XAF Blazor, Web API Service, and Windows Forms applications, you can register your favorite .NET IoC library instead of Microsoft's `IServiceProvider`. For this purpose, you can call the `UseServiceProviderFactory` extension method of the application builder class.

```csharp
var builder = WinApplication.CreateBuilder();
builder.UseServiceProviderFactory(new AutofacServiceProviderFactory());
// OR
// builder.UseServiceProviderFactory(new DryIoCServiceProviderFactory());
```
