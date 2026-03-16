---
uid: DevExpress.ExpressApp.Blazor.ApplicationBuilder.NotificationsApplicationBuilderExtensions.AddNotifications(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder},System.Action{DevExpress.ExpressApp.Notifications.Blazor.NotificationsOptions})
name: AddNotifications(IModuleBuilder<IBlazorApplicationBuilder>, Action<NotificationsOptions>)
type: Method
summary: Adds the [Notifications Module](xref:113688) to your application.
syntax:
  content: public static IModuleBuilder<IBlazorApplicationBuilder> AddNotifications(this IModuleBuilder<IBlazorApplicationBuilder> builder, Action<NotificationsOptions> configureOptions)
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder}
    description: Allows you to register and configure Modules in your application, and chain further Module registrations.
  - id: configureOptions
    type: System.Action{DevExpress.ExpressApp.Notifications.Blazor.NotificationsOptions}
    description: Options that you can use to configure the Notifications Module.
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder}
    description: Allows you to register and configure Modules in your application, and chain further Module registrations.
seealso: []
---
The following example demonstrates how to call this method in your XAF ASP.NET Core Blazor application:

[!include[blazor-notifications-options](~/templates/blazor-notifications-options.md)]