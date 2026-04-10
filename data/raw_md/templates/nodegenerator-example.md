To customize the content of the **<:0:>** node, implement a Generator Updater for this Nodes Generator by inheriting the [](xref:DevExpress.ExpressApp.Model.ModelNodesGeneratorUpdater`1) class in the following manner:

# [C#](#tab/tabid-csharp)

```csharp
public class Updater : ModelNodesGeneratorUpdater<<:1:>> {
    public override void UpdateNode(ModelNode node) {
        // Cast the 'node' parameter to IModel<:0:>
        // to access the <:0:> node.
    }
}
```
***