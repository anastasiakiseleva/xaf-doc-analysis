---
uid: DevExpress.ExpressApp.Utils.CompoundNameConvertStyle
name: CompoundNameConvertStyle
type: Enum
summary: Contains values specifying how compound names can be processed.
syntax:
  content: public enum CompoundNameConvertStyle
seealso: []
---
Compound names consist from several capitalized words glued together. Examples of such names are **BusinessClass**, **RestoreDefaultSettings**, **MyApplicationModule** and so on. The **CompoundNameConvertStyle** enumeration contains values that specify how such names can be processed at various points in an **XAF** application.

You can use the [CaptionHelper.ConvertCompoundName](xref:DevExpress.ExpressApp.Utils.CaptionHelper.ConvertCompoundName*) method, to convert a compound name according to a specified **CompoundNameConvertStyle** mode.