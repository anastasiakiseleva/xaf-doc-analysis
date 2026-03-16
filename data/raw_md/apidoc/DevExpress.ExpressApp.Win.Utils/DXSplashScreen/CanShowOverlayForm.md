---
uid: DevExpress.ExpressApp.Win.Utils.DXSplashScreen.CanShowOverlayForm
name: CanShowOverlayForm
type: Property
summary: Indicates if the current @DevExpress.ExpressApp.Win.Utils.DXSplashScreen instance can show an [Overlay Form](xref:120029).
syntax:
  content: public bool CanShowOverlayForm { get; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if both conditions apply: the [DXSplashScreen.OverlayFormOptions](xref:DevExpress.ExpressApp.Win.Utils.DXSplashScreen.OverlayFormOptions) property is not _null_ and no other applicable [splash form](xref:112680) is currently shown; otherwise, **false**.'
seealso:
- linkId: "112680"
---
The **DXSplashScreen.OverlayFormOptions** property is not _null_ when a @DevExpress.ExpressApp.Win.Utils.DXSplashScreen is initialized with a constructor that takes the _overlayFormOptions_ parameter. 
