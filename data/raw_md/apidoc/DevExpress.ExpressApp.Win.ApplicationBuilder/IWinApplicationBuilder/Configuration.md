---
uid: DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder.Configuration
name: Configuration
type: Property
summary: Returns a @Microsoft.Extensions.Configuration.ConfigurationManager object.
syntax:
  content: ConfigurationManager Configuration { get; }
  parameters: []
  return:
    type: Microsoft.Extensions.Configuration.ConfigurationManager
    description: An application configuration object.
seealso: []
---
XAF registers the `ConfigurationManager` object returned by this property as `IConfiguration` in the @DevExpress.ExpressApp.ApplicationBuilder.IXafApplicationBuilder`1.Services collection.
s