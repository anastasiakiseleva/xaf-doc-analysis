## Prerequisites

Make sure that the following conditions are met:

1. Your project contains the **DevExpress.ExpressApp.ConditionalAppearance** NuGet package.
2. The _MySolution.Blazor.Server\Startup.cs_ or _MySolution.Win\Startup.cs_ files contain the following line:

    ```csharp
    builder.Modules
        // ...
        .AddConditionalAppearance()
    // ...
    ```

For more information on how to add the Conditional Appearance Module, see: [](xref:113286).
