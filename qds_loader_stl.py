#!/bin/env python
import os, sys
import argparse
import logging
import vtk

global gDB
global gArgs
global gTarget

def render(gTarget):
    # Create a rendering window and renderer
    ren = vtk.vtkRenderer()
    renWin = vtk.vtkRenderWindow()
    renWin.AddRenderer(ren)
    # Create a RenderWindowInteractor to permit manipulating the camera
    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    style = vtk.vtkInteractorStyleTrackballCamera()
    iren.SetInteractorStyle(style)

    polydata = loadStl(gTarget)
    ren.AddActor(polyDataToActor(polydata))
    ren.SetBackground(0.1, 0.1, 0.1)

    # enable user interface interactor
    iren.Initialize()
    renWin.Render()
    iren.Start()

def loadStl(fname):
    """Load the given STL file, and return a vtkPolyData object for it."""
    reader = vtk.vtkSTLReader()
    reader.SetFileName(fname)
    reader.Update()
    polydata = reader.GetOutput()
    return polydata

def polyDataToActor(polydata):
    """Wrap the provided vtkPolyData object in a mapper and an actor, returning
    the actor."""
    mapper = vtk.vtkPolyDataMapper()
    if vtk.VTK_MAJOR_VERSION <= 5:
        #mapper.SetInput(reader.GetOutput())
        mapper.SetInput(polydata)
    else:
        mapper.SetInputData(polydata)
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    #actor.GetProperty().SetRepresentationToWireframe()
    actor.GetProperty().SetColor(0.5, 0.5, 1.0)
    return actor

def verify():
    global gArgs
    global gDb
    global gTarget
    parser = argparse.ArgumentParser(description='qds_loader_stl')
    parser.add_argument('stl', nargs='*', default=None)
    parser.add_argument('-v', '--verbose', dest='verbose', action = 'store_true', default=False, help='Verbose mode')
    gArgs = parser.parse_args()
    gTarget = ' '.join(gArgs.stl)
    log_level = logging.INFO
    if gArgs.verbose:
        log_level = logging.DEBUG
    if not gTarget:
        parser.print_help()
        exit()
    logging.basicConfig(level=log_level)
    gDb = logging.getLogger(__name__)

def main():
    global gTarget
    render(gTarget)

if __name__ == '__main__':
    verify()
    main()
