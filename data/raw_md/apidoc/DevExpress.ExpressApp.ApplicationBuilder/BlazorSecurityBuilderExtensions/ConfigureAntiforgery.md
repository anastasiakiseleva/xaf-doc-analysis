---
uid: DevExpress.ExpressApp.ApplicationBuilder.BlazorSecurityBuilderExtensions.ConfigureAntiforgery(DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorSecurityBuilder,System.Action{DevExpress.ExpressApp.Security.AntiforgeryValidationOptions})
name: ConfigureAntiforgery(IBlazorSecurityBuilder, Action<AntiforgeryValidationOptions>)
type: Method
summary: ''
syntax:
  content: public static IBlazorSecurityBuilder ConfigureAntiforgery(this IBlazorSecurityBuilder builder, Action<AntiforgeryValidationOptions> configureOptions)
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorSecurityBuilder
    description: ''
  - id: configureOptions
    type: System.Action{DevExpress.ExpressApp.Security.AntiforgeryValidationOptions}
    description: ''
  return:
    type: DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorSecurityBuilder
    description: ''
seealso: []
---
> [!important]
> The Antiforgery mechanism in Web API apps with Windows authentication can result in error 400. You can use the `AntiforgeryOptions.ExcludeAuthenticationSchemes` property to disable antiforgery for Windows authentication:
> 
> ```csharp
> builder.Security
    .UseIntegratedMode(options => {...})
    .ConfigureAntiforgery(opt => {
        opt.ExcludeAuthenticationSchemes.Add("NTLM"); // for Kestrel
        opt.ExcludeAuthenticationSchemes.Add("Negotiate"); // for IIS
    });
```