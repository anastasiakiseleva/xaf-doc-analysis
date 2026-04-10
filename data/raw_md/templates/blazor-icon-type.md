`Auto`
:   Default value. XAF switches icons according to the currently selected theme.
`Blazor`
:   XAF uses icons from the Classic theme set.
`Fluent`
:   XAF uses icons from the Fluent theme set.

# [MySolution.Blazor.Server\MySolutionBlazorApplication.cs](#tab/tabid-cs)
```csharp{7}
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor;

public class MySolutionBlazorApplication : BlazorApplication {
    public MySolutionBlazorApplication() {
        // ...
        IconType = IconType.Fluent;
    }
}
```
***

> [!ImageGallery]
> ![An XAF application with the Fluent icon set](~/images/xaf-blazor-fluent-icons.png)
> ![An XAF application with the Standard icon set](~/images/xaf-blazor-standard-icons.png)