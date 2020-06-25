#pragma once

#ifdef GAME_ENGINE_WINDOWNS
	#ifdef GAME_ENGINE_BUILD_DLL
		#define GAME_ENGINE_API as _declspec(dllexport)
	#else
		#define GAME_ENGINE_API as _declspec(dllimport)
	#endif 

#else
	#error Game engine  only support windows !
#endif // GAME_ENGINE_WINDOWNS
