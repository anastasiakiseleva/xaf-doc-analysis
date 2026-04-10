## Usage Considerations

In most cases, it is highly recommended that you use @DevExpress.ExpressApp.Services.Localization.ICaptionHelperProvider rather than the static API exposed by the @DevExpress.ExpressApp.Utils.CaptionHelper class. Note that the `CaptionHelper` static API is not supported in [Backend Web API Service](xref:403394) as well as the [Reports](xref:113591) and [Dashboards](xref:117449) modules. Additionally, if your business objects are used in Web API, dashboards, or reports, these business objects should also exclusively use `ICaptionHelperProvider`.

The `CaptionHelper` static API is required to obtain user-specific localized strings from a user [Model Differences Storage](xref:112580#application-model-differences-storage-types). However, you can only use it in contexts where [XafApplication](xref:DevExpress.ExpressApp.XafApplication) is initialized, such as:

- [XAF controllers](xref:112621)
- [Custom property editors](xref:113097)
- [Application modules](xref:118046)