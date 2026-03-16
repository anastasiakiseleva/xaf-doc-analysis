---
uid: "403360"
title: 'How to: Use a Custom Action to Upload a File in a Popup Window'
owner: Eugenia Simonova
---
# How to: Use a Custom Action to Upload a File in a Popup Window

The following example shows a popup window to upload a file and save it to a stream. 

![|Popup Window to Upload a File](~/images/use-custom-action-to-upload-file.png)

> [!NOTE]
> For more information on how to download a file in XAF Blazor apps, refer to the following topic: [](xref:404760).

1. Add the File Attachments Module to your application as described in the following section:
 [Add File Attachments Module to an XAF Application](xref:112781#add-the-file-attachments-module-to-an-xaf-application)

2. Create  the _UploadFileParameters_ class with the _File_ property of the **FileData** type. XAF shows **FileDataPropertyEditor** for this property type. For more information, see the following help topic: [File Attachment Properties](xref:113548).

3. Use an instance of the @DevExpress.ExpressApp.Actions.PopupWindowShowAction class to show a popup window.

4. Handle the @DevExpress.ExpressApp.Actions.PopupWindowShowAction.Execute event and call the [](xref:DevExpress.Persistent.Base.IFileData.SaveToStream(System.IO.Stream)) method to save the file to a stream. Note that the gzip compression is applied to the saved byte array.

# [C#](#tab/tabid-csharp)

```csharp
using System.IO;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.DC;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF; // For XPO, replace with 'using DevExpress.Persistent.BaseImpl;'.
using DevExpress.Persistent.Validation;

namespace XafUploadButton.Module.Controllers {
    public partial class UploadInPopupController : ViewController {
        public UploadInPopupController() {
            var customUploadFileAction = new PopupWindowShowAction(this,"CustomUploadFileAction", PredefinedCategory.View){
                Caption = "Custom Upload",
                ImageName = "AddFile"
            };
            customUploadFileAction.Execute += CustomUploadFileAction_Execute;
            customUploadFileAction.CustomizePopupWindowParams += CustomUploadFileAction_CustomizePopupWindowParams;
        }
        private void CustomUploadFileAction_Execute(object sender, PopupWindowShowActionExecuteEventArgs e) {
            FileData fileData = ((UploadFileParameters)e.PopupWindowViewCurrentObject).File;
            using(var stream = new MemoryStream()) {
                fileData.SaveToStream(stream);
                stream.Position = 0;
                // Perform your operations with the stream.
            }
        }
        private void CustomUploadFileAction_CustomizePopupWindowParams(object sender, CustomizePopupWindowParamsEventArgs e) {
            NonPersistentObjectSpace os = (NonPersistentObjectSpace)e.Application.CreateObjectSpace(typeof(UploadFileParameters));
            os.PopulateAdditionalObjectSpaces(Application);
            e.DialogController.SaveOnAccept = false;
            e.View = e.Application.CreateDetailView(os, os.CreateObject<UploadFileParameters>());
        }
    }
    [DomainComponent]
    public class UploadFileParameters : NonPersistentObjectImpl {
        private FileData file;
        [ExpandObjectMembers(ExpandObjectMembers.Never)]
        [RuleRequiredField("", "Save", "File should be assigned")]
        public FileData File {
            get { return file; }
            set { SetPropertyValue(ref file, value); }
        }
    }
}
```
***

[`PopupWindowShowAction`]: xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction
[`/\.(Execute)/`]: xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction.Execute
[`/\.(CustomizePopupWindowParams)/`]: xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction.CustomizePopupWindowParams
[`Caption`]: xref:DevExpress.ExpressApp.Actions.ActionBase.Caption
[`ImageName`]: xref:DevExpress.ExpressApp.Actions.ActionBase.ImageName
[`SaveToStream`]: xref:DevExpress.Persistent.Base.IFileData.SaveToStream(System.IO.Stream)
[`PopupWindowShowActionExecuteEventArgs`]: xref:DevExpress.ExpressApp.Actions.PopupWindowShowActionExecuteEventArgs
[`PopupWindowViewCurrentObject`]: xref:DevExpress.ExpressApp.Actions.PopupWindowShowActionExecuteEventArgs.PopupWindowViewCurrentObject
[`MemoryStream`]: xref:System.IO.MemoryStream.#ctor
[`NonPersistentObjectSpace`]: xref:DevExpress.ExpressApp.NonPersistentObjectSpace
[`DomainComponent`]: xref:DevExpress.ExpressApp.DC.DomainComponentAttribute
[`ExpandObjectMembers`]: xref:DevExpress.Persistent.Base.ExpandObjectMembersAttribute
[`ExpandObjectMembers.Never`]: xref:DevExpress.Persistent.Base.ExpandObjectMembers.Never
[`RuleRequiredField`]: xref:DevExpress.Persistent.Validation.RuleRequiredFieldAttribute
