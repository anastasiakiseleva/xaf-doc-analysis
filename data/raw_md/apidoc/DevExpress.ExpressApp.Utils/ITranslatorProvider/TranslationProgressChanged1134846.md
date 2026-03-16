---
uid: DevExpress.ExpressApp.Utils.ITranslatorProvider.TranslationProgressChanged
name: TranslationProgressChanged
type: Event
summary: Occurs when it is required to update the progress bar displayed when the translation is performed.
syntax:
  content: event EventHandler<TranslationProgressEventArgs> TranslationProgressChanged
seealso: []
---
The **Progress** parameter of the event arguments may be within the 0…1 range. You can also cancel the translation by setting the **Cancel** parameter to **True**.