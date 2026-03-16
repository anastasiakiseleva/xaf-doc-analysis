---
uid: DevExpress.ExpressApp.Office.Win.IRichTextValueStorage
name: IRichTextValueStorage
type: Interface
summary: Declares members of the Rich Text editor's value storage.
syntax:
  content: public interface IRichTextValueStorage
seealso:
- linkId: DevExpress.ExpressApp.Office.Win.IRichTextValueStorage._members
  altText: IRichTextValueStorage Members
---
A Rich Text editor's value storage allows you to implement custom logic executed when saving or loading a RichText document. Follow the steps below to create a custom value storage that overrides a file storage format.

1. Create a class that implements the `IRichTextValueStorage` interface as shown below in the [WinForms application project](xref:118045) (_MySolution.Win_).

    # [C#](#tab/tabid-csharp)
    ```csharp
    using DevExpress.ExpressApp.Office.Win;
    using DevExpress.XtraRichEdit;
    //..
    public class MhtRichTextValueStorage : IRichTextValueStorage {
        public object GetValue(RichEditControl control) {
            return control.MhtText;
        }
        public void SetValue(RichEditControl control, object propertyValue) {
            control.MhtText = (string)propertyValue;
        }
    }
    ```
    ***

2. Create a [View Controller](xref:112621#view-controllers) and access the `RichTextPropertyEditor` as described in the [Ways to Access UI Elements and Their Controls](xref:120092#get-the-viewitem-or-property-editor-object) topic. Set the editor's `ValueStorage` property to an instance of `CustomRichTextValueStorage` as shown below:

    # [C#](#tab/tabid-csharp)
    ```csharp
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Office.Win;
    // ...
    public class RichTextValueStorageController : ObjectViewController<DetailView, Document> {
        protected override void OnActivated() {
            base.OnActivated();
            RichTextPropertyEditor richTextPropertyEditor = View.FindItem("Text") as RichTextPropertyEditor;
            if (richTextPropertyEditor != null) {
                richTextPropertyEditor.ValueStorage = new MhtRichTextValueStorage();
            }
        }
    }
    ```
    ***   