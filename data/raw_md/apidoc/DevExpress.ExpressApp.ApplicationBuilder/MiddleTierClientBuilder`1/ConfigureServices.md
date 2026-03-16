---
uid: DevExpress.ExpressApp.ApplicationBuilder.MiddleTierClientBuilder`1.ConfigureServices(System.Action{Microsoft.Extensions.DependencyInjection.IServiceCollection})
name: ConfigureServices(Action<IServiceCollection>)
type: Method
summary: Allows you to replace default services or register additional custom services used in a Middle Tier client.
syntax:
  content: public MiddleTierClientBuilder<TDbContext> ConfigureServices(Action<IServiceCollection> configure)
  parameters:
  - id: configure
    type: System.Action{Microsoft.Extensions.DependencyInjection.IServiceCollection}
    description: A delegate that allows you to replace default services or register additional custom services.
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.MiddleTierClientBuilder{{TDbContext}}
    description: The builder that allows you to further configure the Middle Tier client.
seealso:
- linkId: "404389"
- linkId: "404398"
---
