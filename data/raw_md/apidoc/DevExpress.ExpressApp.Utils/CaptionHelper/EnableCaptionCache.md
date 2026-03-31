---
uid: DevExpress.ExpressApp.Utils.CaptionHelper.EnableCaptionCache
name: EnableCaptionCache
type: Field
summary: Specifies if XAF caches class and member captions for all locales.
syntax:
  content: public static bool EnableCaptionCache
  return:
    type: System.Boolean
    description: If `true`, XAF caches class and member captions for all locales. If `false`, XAF loads class and member captions from the application model.
seealso: []
defaultMemberValue: 'true'
---
Disable this property if your Application Model has specific caption settings stored in the [user differences](xref:112580#application-model-layers) layer (individual user settings).