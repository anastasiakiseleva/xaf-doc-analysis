---
uid: DevExpress.Persistent.Base.General.ITreeNodeSvgImageProvider.GetSvgImage(System.String@)
name: GetSvgImage(out String)
type: Method
summary: Returns the SVG image corresponding to a tree node.
syntax:
  content: SvgImage GetSvgImage(out string imageName)
  parameters:
  - id: imageName
    type: System.String
    description: A string holding the returned SVG image's name.
  return:
    type: DevExpress.Utils.Svg.SvgImage
    description: A **DevExpress.Utils.Svg.SvgImage** object representing the SVG image corresponding to a tree node.
seealso: []
---
This method returns a **DevExpress.Utils.Svg.SvgImage** object representing the SVG image corresponding to a [Tree List](xref:112836)'s node.
Specify the **imageName** parameter only if you are using the same image for multiple nodes. Otherwise, assign 'null'.