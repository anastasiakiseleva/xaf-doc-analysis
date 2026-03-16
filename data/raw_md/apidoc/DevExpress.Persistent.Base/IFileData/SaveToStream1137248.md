---
uid: DevExpress.Persistent.Base.IFileData.SaveToStream(System.IO.Stream)
name: SaveToStream(Stream)
type: Method
summary: Saves the file stored within the current [](xref:DevExpress.Persistent.Base.IFileData) object to the specified stream.
syntax:
  content: void SaveToStream(Stream stream)
  parameters:
  - id: stream
    type: System.IO.Stream
    description: A [Stream](https://learn.microsoft.com/en-us/dotnet/api/system.io.stream) object to be used to save the file.
seealso: []
---
The example below demonstrates how to use the **SaveToStream** method to get a Contact's file, and then upload it into a portfolio.

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
