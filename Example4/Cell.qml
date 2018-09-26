import QtQuick 2.0

// Item is the most basic QML type and is often used a container fro other types
Item {
    id: container
    // Here we declare the cellColor property which is accessible outside of our component
    // This allows us to make Cells with different colors, this is also an alias for an existing property
    property alias cellColor: rectangle.color
    // Here we declared a signal we call clicked which has a parameter by the name cellColor of type color
    // We will use this signal to change the color of the main QML file
    signal clicked(color cellColor)

    width: 40; height: 25
    // Our cell is basically a colored rectangle with the id rectangle
    // the ancrhos.fill propery is a convienient way to set the size. In this case the 
    // Rectangle will have the same size as the parent Item
    Rectangle {
        id: rectangle
        border.color: "white"
        anchors.fill: parent
    }
    // in order to triger the signal we need to make a MouseArea that is the same size as the parent
    // When the signal is triggeres we want to emit our clicked signal with the color as a parameter
    MouseArea {
        anchors.fill: parent
        onClicked: container.clicked(container.cellColor)
    }
}