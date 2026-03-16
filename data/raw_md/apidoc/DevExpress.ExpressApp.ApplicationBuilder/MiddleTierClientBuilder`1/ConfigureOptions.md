---
uid: DevExpress.ExpressApp.ApplicationBuilder.MiddleTierClientBuilder`1.ConfigureOptions(System.Action{DevExpress.ExpressApp.ApplicationBuilder.EFCoreMiddleTierSecurityOptions})
name: ConfigureOptions(Action<EFCoreMiddleTierSecurityOptions>)
type: Method
summary: Configures client connection options to the Middle Tier server.
syntax:
  content: public MiddleTierClientBuilder<TDbContext> ConfigureOptions(Action<EFCoreMiddleTierSecurityOptions> configure)
  parameters:
  - id: configure
    type: System.Action{DevExpress.ExpressApp.ApplicationBuilder.EFCoreMiddleTierSecurityOptions}
    description: A delegate that configures [EF Core Middle Tier Security](xref:404389) options.
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.MiddleTierClientBuilder{{TDbContext}}
    description: The builder that allows you to further configure the Middle Tier Security client.
seealso:
- linkId: "404389"
- linkId: "404398"
---
