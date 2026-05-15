---
uid: DevExpress.ExpressApp.FileAttachments.Win.FileAttachmentsWindowsFormsModule.GetFileDataManager(DevExpress.ExpressApp.XafApplication)
name: GetFileDataManager(XafApplication)
type: Method
summary: Provides access to the file data manager used by the [](xref:DevExpress.ExpressApp.FileAttachments.Win.FileAttachmentsWindowsFormsModule).
syntax:
  content: public static IFileDataManager GetFileDataManager(XafApplication application)
  parameters:
  - id: application
    type: DevExpress.ExpressApp.XafApplication
    description: An [](xref:DevExpress.ExpressApp.XafApplication) object that provides methods and properties to manage the current application.
  return:
    type: DevExpress.ExpressApp.FileAttachments.Win.IFileDataManager
    description: An **IFileDataManager** object that can be used to open stored files using an associated application or to save them to a local disk.
seealso: []
---
The following code snippet demonstrates an [Action](xref:112622) that opens all resume files. The Action is designed for [List Views](xref:112611) of the **Resume** business class, which is declared in the MainDemo installed in the _[!include[PathToMainDemo](~/templates/path-to-main-demo-ef-core.md)]_ folder, by default.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.FileAttachments.Win;
//...
public class MyViewController : ViewController<ListView> {
    SimpleAction openSelectedDocuments;
    public MyViewController() {
        TargetObjectType = typeof(Resume);
        openSelectedDocuments = new SimpleAction(
            this, "OpenSelectedDocumentsAction", "RecordEdit", openSelectedDocuments_Execute);
        openSelectedDocuments.Caption = "Open Selected Documents";
        openSelectedDocuments.SelectionDependencyType = 
            SelectionDependencyType.RequireMultipleObjects;
    }
    void openSelectedDocuments_Execute(object sender, SimpleActionExecuteEventArgs e) {
        foreach (Resume resume in View.SelectedObjects) {
            if (resume.File != null) {
                FileAttachmentsWindowsFormsModule.GetFileDataManager(Application).Open(resume.File);
            }
        }
    }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.ExpressApp
Imports DevExpress.ExpressApp.Actions
Imports DevExpress.ExpressApp.FileAttachments.Win
'...
Public Class MyViewController
    Inherits ViewController(Of ListView)
    Private openSelectedDocuments As SimpleAction
    Public Sub New()
        TargetObjectType = GetType(Resume)
        openSelectedDocuments = New SimpleAction( _
        Me, "OpenSelectedDocumentsAction", "RecordEdit", AddressOf openSelectedDocuments_Execute)
        openSelectedDocuments.Caption = "Open Selected Documents"
        openSelectedDocuments.SelectionDependencyType = _
        SelectionDependencyType.RequireMultipleObjects
    End Sub
    Private Sub openSelectedDocuments_Execute( _
    ByVal sender As Object, ByVal e As SimpleActionExecuteEventArgs)
        For Each [resume] As [Resume] In View.SelectedObjects
            If [resume].File IsNot Nothing Then
                FileAttachmentsWindowsFormsModule.GetFileDataManager( _ 
                Application).Open([resume].File)
            End If
        Next [resume]
    End Sub
End Class
```

***