// Fill out your copyright notice in the Description page of Project Settings.

#include "ReadFileBlueprintFunctionLibrary.h"


 bool UReadFileBlueprintFunctionLibrary::FileSaveString(FString SaveTextB, FString FileNameB)
 {
     return FFileHelper::SaveStringToFile(SaveTextB, *(FPaths::GameDir() + FileNameB));
 }
 
 bool UReadFileBlueprintFunctionLibrary::FileLoadString(FString FileNameA, FString& SaveTextA)
 {
     return FFileHelper::LoadFileToString(SaveTextA, *(FPaths::GameDir() + FileNameA));
 }



