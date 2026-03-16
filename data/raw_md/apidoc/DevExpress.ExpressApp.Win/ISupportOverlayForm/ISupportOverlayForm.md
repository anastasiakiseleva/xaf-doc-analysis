---
uid: DevExpress.ExpressApp.Win.ISupportOverlayForm
name: ISupportOverlayForm
type: Interface
summary: Provides methods to show and close an [Overlay Form](xref:120029).
syntax:
  content: public interface ISupportOverlayForm
seealso:
- linkId: DevExpress.ExpressApp.Win.ISupportOverlayForm._members
  altText: ISupportOverlayForm Members
---
The @DevExpress.ExpressApp.Win.WinApplication class uses the **ISupportOverlayForm** interface to [show](xref:DevExpress.ExpressApp.Win.WinApplication.StartOverlayForm*) and [stop](xref:DevExpress.ExpressApp.Win.ISupportOverlayForm.StopOverlayForm*) the Overlay Form. Implement this interface in your code if you [use a custom class](xref:112680) instead of @DevExpress.ExpressApp.Win.Utils.DXSplashScreen to show splash forms.

For more details on how to show the Overlay Form, refer to the [Splash Forms](xref:112680) article.