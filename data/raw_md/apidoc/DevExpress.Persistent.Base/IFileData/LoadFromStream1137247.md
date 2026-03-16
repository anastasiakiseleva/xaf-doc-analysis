---
uid: DevExpress.Persistent.Base.IFileData.LoadFromStream(System.String,System.IO.Stream)
name: LoadFromStream(String, Stream)
type: Method
summary: Loads the file data from a stream.
syntax:
  content: void LoadFromStream(string fileName, Stream stream)
  parameters:
  - id: fileName
    type: System.String
    description: A string that is the file name.
  - id: stream
    type: System.IO.Stream
    description: A [Stream](https://learn.microsoft.com/en-us/dotnet/api/system.io.stream) that is the file content.
seealso:
- linkId: "112781"
- linkId: 113142#file-attachments-module
  altText: File Attachments Module Controllers
---
The example below demonstrates how to use the **LoadFromStream** method to upload a Contact's file into a portfolio.

# [C#](#tab/tabid-csharp)

```csharp
using System.IO;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
using MainDemo.Module.BusinessObjects;
// ...
public class UpdatePortfolioController : ObjectViewController<DetailView, Resume> {
    public UpdatePortfolioController() {
        SimpleAction updatePortfolioAction = new SimpleAction(this, "UpdatePortfolio", PredefinedCategory.Edit);
        updatePortfolioAction.SelectionDependencyType = SelectionDependencyType.RequireSingleObject;
        updatePortfolioAction.Execute += updatePortfolioAction_Execute;
    }
    private void updatePortfolioAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
        FileData currentFile = ViewCurrentObject.File;
        if(currentFile != null && !currentFile.IsEmpty) {
            FileData fileCopy = ObjectSpace.CreateObject<FileData>();
            using(var stream = new MemoryStream()) {
                currentFile.SaveToStream(stream);
                stream.Position = 0;
                fileCopy.LoadFromStream(currentFile.FileName, stream);
            }
            PortfolioFileData portfolio = ObjectSpace.CreateObject<PortfolioFileData>();
            portfolio.File = fileCopy;
            ViewCurrentObject.Portfolio.Add(portfolio);
            ObjectSpace.CommitChanges();
        }
    }
}
```
***

Here, **FileData** is a built-in class that implements the [](xref:DevExpress.Persistent.Base.IFileData) interface.

