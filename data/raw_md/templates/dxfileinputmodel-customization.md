**File:** _MySolution.Blazor.Server\Controllers\CustomizeFileSizeController.cs_

```csharp
using DevExpress.ExpressApp.FileAttachments.Blazor.Editors;
using DevExpress.ExpressApp;
using MySolution.Module.BusinessObjects;

namespace MySolution.Blazor.Server.Controllers;
public class CustomizeFileSizeController : ObjectViewController<DetailView, Resume> {
    protected override void OnActivated() {
        View.CustomizeViewItemControl<DxFileDataPropertyEditor>(this, editor => {
            editor.ComponentModel.AcceptedFileTypes = [".jpg", ".gif"];
            editor.ComponentModel.MaxFileSize = 1024 * 512;
        });
    }
}
```